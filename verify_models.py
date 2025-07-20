#!/usr/bin/env python3
"""
Verify available Gemini models
"""

import asyncio
import os
import signal
import google.generativeai as genai

async def test_model_with_timeout(model_name, timeout=10):
    """Test a model with timeout."""
    try:
        print(f"Testing {model_name}...", end=" ", flush=True)
        
        # Create model
        model = genai.GenerativeModel(model_name)
        
        # Test with timeout
        try:
            response = await asyncio.wait_for(
                asyncio.to_thread(model.generate_content, "Hello"),
                timeout=timeout
            )
            
            if response and response.text:
                print("✅ Available")
                return True
            else:
                print("❌ No response")
                return False
                
        except asyncio.TimeoutError:
            print("⏰ Timeout")
            return False
            
    except Exception as e:
        error_msg = str(e)
        if "not found" in error_msg.lower() or "doesn't exist" in error_msg.lower():
            print("❌ Not available")
        elif "quota" in error_msg.lower():
            print("❌ Quota exceeded")
        elif "key" in error_msg.lower():
            print("❌ Invalid API key")
        else:
            print(f"❌ Error: {error_msg[:30]}...")
        return False

async def verify_models():
    """Verify which Gemini models are available."""
    
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY environment variable not set")
        print("Please set your Gemini API key:")
        print("export GEMINI_API_KEY='your_api_key_here'")
        return
    
    print("🔍 Verifying available Gemini models...")
    print("=" * 50)
    
    # Configure Gemini
    genai.configure(api_key=api_key)
    
    # Test models in order of preference
    models_to_test = [
        "gemini-2.5-flash",
        "gemini-2.5-pro", 
        "gemini-2.0-flash",
        "gemini-2.0-pro",
        "gemini-1.5-flash",
        "gemini-1.5-pro"
    ]
    
    available_models = []
    
    for model_name in models_to_test:
        is_available = await test_model_with_timeout(model_name, timeout=15)
        if is_available:
            available_models.append(model_name)
        
        # Small delay between tests
        await asyncio.sleep(0.5)
    
    print("\n" + "=" * 50)
    print("📋 Summary:")
    print(f"Available models: {len(available_models)}")
    
    if available_models:
        for model in available_models:
            print(f"  ✅ {model}")
        print(f"\n🎯 Recommended default: {available_models[0]}")
        print(f"💡 For best quality, use: {available_models[0].replace('-flash', '-pro') if '-flash' in available_models[0] else available_models[0]}")
    else:
        print("⚠️  No models available.")
        print("\n🔧 Troubleshooting:")
        print("1. Check your API key is correct")
        print("2. Verify you have sufficient quota")
        print("3. Check your internet connection")
        print("4. Try again later (API might be temporarily unavailable)")

def signal_handler(signum, frame):
    print("\n\n⏹️  Verification interrupted by user")
    exit(0)

if __name__ == "__main__":
    # Set up signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    try:
        asyncio.run(verify_models())
    except KeyboardInterrupt:
        print("\n\n⏹️  Verification interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}") 
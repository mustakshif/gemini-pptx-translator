#!/usr/bin/env python3
"""
Quick test for Gemini models - tests only the most common models
"""

import asyncio
import os
import google.generativeai as genai

async def quick_test():
    """Quick test of the most common Gemini models."""
    
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY not set")
        return
    
    print("⚡ Quick Gemini Model Test")
    print("=" * 30)
    
    # Configure Gemini
    genai.configure(api_key=api_key)
    
    # Test only the most common models
    models = [
        "gemini-2.5-flash",
        "gemini-1.5-flash", 
        "gemini-1.5-pro"
    ]
    
    for model_name in models:
        try:
            print(f"Testing {model_name}...", end=" ", flush=True)
            
            model = genai.GenerativeModel(model_name)
            response = model.generate_content("Hi")
            
            if response and response.text:
                print("✅ Works")
            else:
                print("❌ No response")
                
        except Exception as e:
            error = str(e).lower()
            if "not found" in error or "doesn't exist" in error:
                print("❌ Not available")
            elif "quota" in error:
                print("❌ Quota exceeded")
            else:
                print("❌ Error")
        
        # Brief pause
        await asyncio.sleep(1)
    
    print("\n✅ Quick test completed!")

if __name__ == "__main__":
    asyncio.run(quick_test()) 
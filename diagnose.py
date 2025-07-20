#!/usr/bin/env python3
"""
Diagnose Gemini API connection and basic functionality
"""

import os
import asyncio
import google.generativeai as genai

async def diagnose():
    """Diagnose Gemini API connection."""
    
    print("🔍 Gemini API Diagnosis")
    print("=" * 40)
    
    # Check API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("❌ GEMINI_API_KEY not set")
        print("Please set: export GEMINI_API_KEY='your_key'")
        return False
    
    print("✅ API key found")
    
    # Test basic connection
    try:
        genai.configure(api_key=api_key)
        print("✅ Gemini configured")
    except Exception as e:
        print(f"❌ Configuration failed: {e}")
        return False
    
    # Test with a simple model
    try:
        print("🔧 Testing basic connection...", end=" ", flush=True)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Hello")
        
        if response and response.text:
            print("✅ Connection successful")
            return True
        else:
            print("❌ No response")
            return False
            
    except Exception as e:
        error = str(e).lower()
        if "quota" in error:
            print("❌ Quota exceeded")
        elif "key" in error:
            print("❌ Invalid API key")
        elif "not found" in error:
            print("❌ Model not available")
        else:
            print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(diagnose())
    if success:
        print("\n🎉 Diagnosis passed! You can now use the translation script.")
    else:
        print("\n⚠️  Diagnosis failed. Please check your setup.") 
# PPTX Translate with Gemini API (Fixed Version)

**Language:** [English](README.md) | [中文](README_zh.md)

PowerPoint presentation translator using Google Gemini API with improved text extraction algorithms and intelligent progress tracking.

> **Reference:** This project is inspired by and references [@thiagoperes/pptx-translate](https://github.com/thiagoperes/pptx-translate)

## Features

- High-quality translation using Google Gemini API
- **Improved text extraction algorithm** - Extract complete paragraphs to avoid format corruption
- **Intelligent progress tracking system** - Real-time progress display, ETA calculation, and progress bars
- Support for latest Gemini models (including Gemini 2.5 series)
- Extract text content from PowerPoint (titles, body text, table cells)
- **Asynchronous batch translation** - Efficiently process large amounts of text content
- **Smart caching mechanism** - Avoid duplicate API calls, support resume capability
- **Enhanced error handling** - Timeout controls, quota detection, automatic retry
- **Format preservation algorithm** - Maintain original text formatting and styles
- Detailed logging and multiple output modes
- Command-line interface supporting single file or batch processing

## Core Algorithm Improvements

### 1. Text Extraction Algorithm Optimization
- **Paragraph-level extraction**: Extract complete paragraphs instead of splitting by text fragments
- **Enhanced table processing**: Complete extraction of table cell content, maintaining data integrity
- **Format preservation**: Retain original formatting and styles during translation

### 2. Intelligent Progress Tracking
- **Real-time progress bar**: Display visual progress bar and percentage
- **ETA calculation**: Estimate remaining time based on current speed
- **Memory optimization**: Efficiently handle progress display for large files

### 3. Asynchronous Translation Engine
- **Batch processing**: Process multiple text elements simultaneously
- **Timeout control**: 30-second API call timeout to prevent hanging
- **Error recovery**: Retain original text when API fails, continue processing

## Supported Gemini Models

### Latest Version (Gemini 2.5) 🆕
- `gemini-2.5-flash`: Latest Gemini 2.5 Flash model (fastest and most efficient, **default recommended**)
- `gemini-2.5-pro`: Latest Gemini 2.5 Pro model (most powerful, suitable for complex translation tasks)

### Experimental Version (Gemini 2.0)
- `gemini-2.0-flash-exp`: Experimental Flash model
- `gemini-2.0-flash`: Stable Flash model  
- `gemini-2.0-pro`: Pro model

### Legacy Version (Gemini 1.5)
- `gemini-1.5-flash`: Legacy Flash model
- `gemini-1.5-pro`: Legacy Pro model
- `gemini-1.5-flash-exp`: Legacy experimental Flash
- `gemini-1.5-pro-exp`: Legacy experimental Pro

## Installation

1. Clone or download project files
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Getting Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Set API key as environment variable:

```bash
export GEMINI_API_KEY="YOUR GEMINI API KEY HERE"
```

## Usage

### Basic Usage

Translate a single file (using default gemini-2.5-flash model):
```bash
python translator.py presentation.pptx -l en
```

Specify output file:
```bash
python translator.py presentation.pptx -l zh-CN -o translated.pptx
```

Use Pro model for high-quality translation:
```bash
python translator.py presentation.pptx -l es -m gemini-2.5-pro
```

### Batch Processing

Translate all PPT files in current directory:
```bash
python translator.py -l fr
```

### View Available Models

```bash
python translator.py --list-models
```

### Verify Model Availability

```bash
# Full verification (may be slow)
python verify_models.py

# Quick verification (recommended)
python quick_test.py

# Basic diagnostics
python diagnose.py
```

### Command Line Arguments

- `input_file`: Input PowerPoint file (.pptx)
- `-l, --language`: Target language code (required)
- `-o, --output`: Output file path
- `-k, --api_key`: Gemini API key (or set GEMINI_API_KEY environment variable)
- `-m, --model`: Gemini model to use (default: gemini-2.5-flash)
- `--list-models`: List available models and exit
- `--profile`: Enable performance profiling and processing time statistics
- `--verbose`: Show detailed translation progress (display each text item)
- `--quiet`: Minimize output (only show errors and final results)

### Supported Language Codes

- `en`: English
- `zh-CN`: Simplified Chinese
- `zh-TW`: Traditional Chinese
- `es`: Spanish
- `fr`: French
- `de`: German
- `ja`: Japanese
- `ko`: Korean
- `ar`: Arabic
- `ru`: Russian
- `pt`: Portuguese
- `it`: Italian
- `nl`: Dutch
- `sv`: Swedish
- And more...

## Usage Examples

### Chinese to English (with progress bar)
```bash
python translator.py presentation.pptx -l en
# Output: Translating to en: ████████████████████████████████████████████████████ 100.0% (45/45) Completed in 23.4s
```

### English to Chinese (verbose mode)
```bash
python translator.py presentation.pptx -l zh-CN -o translated_presentation.pptx --verbose
```

### Use latest Pro model for high-quality translation
```bash
python translator.py presentation.pptx -l es -m gemini-2.5-pro
```

### Performance profiling mode
```bash
python translator.py presentation.pptx -l en --profile
# Shows detailed processing time statistics
```

### Quiet mode (only show results)
```bash
python translator.py presentation.pptx -l en --quiet
```

## Smart Caching System

The script automatically creates translation cache files with the following features:
- **Avoid duplicate translations**: Same text won't call API repeatedly
- **Resume capability**: Continue previous progress after interruption
- **File-specific caching**: Each file and language combination has independent cache

Cache file format:
```
translation_cache_{filename}_{language}_{hash}.json
```

## Logging System

Translation process is recorded to:
- **Console output**: Real-time progress and status information
- **Log file**: `translation_log.txt` - Detailed operation records
- **Progress tracking**: Visual progress bars and ETA time estimation

## Performance Features

### Processing Speed
- **Asynchronous processing**: Concurrent processing of multiple text elements
- **Smart caching**: Avoid duplicate API calls
- **Batch optimization**: Reduce number of API requests

### Error Handling
- **30-second timeout control**: Prevent API calls from hanging
- **Quota detection**: Automatically identify API quota issues
- **Graceful degradation**: Retain original text when API fails

### Memory Optimization
- **Streaming processing**: Process large files progressively
- **Cache management**: Automatically save and load translation cache

## Notes

1. **API quota management**: Ensure sufficient Gemini API quota
2. **File size**: Large file translation may take considerable time, recommend using progress bar mode
3. **Backup recommendation**: Recommend backing up original files before translation
4. **Format compatibility**: Some special PowerPoint formats may not be fully preserved
5. **Network stability**: Ensure stable network connection to avoid API timeouts

## Troubleshooting

### Common Issues

1. **API key error**
   - Check if GEMINI_API_KEY environment variable is correctly set
   - Or use `-k` parameter to provide API key directly
   - Run `python diagnose.py` for basic diagnostics

2. **Model unavailable**
   - Use `--list-models` to view available models
   - Run `python quick_test.py` for quick verification
   - Recommend using default `gemini-2.5-flash` model

3. **Translation progress stuck**
   - Script has added 30-second timeout control
   - Check network connection stability
   - Try using `--verbose` mode to view detailed progress

4. **File reading error**
   - Ensure file path is correct and file is not occupied
   - Check if file is valid PowerPoint format (.pptx)
   - Confirm file permissions allow reading

5. **Translation quality issues**
   - Try using `gemini-2.5-pro` model for better translation quality
   - Check if original text is clear and complete
   - Use `--verbose` mode to check specific translation content

6. **API timeout or quota issues**
   - Check Gemini API quota usage
   - Script has added intelligent retry mechanism
   - Large files can consider batch processing or using cache resume

### Performance Optimization Suggestions

1. **Choose appropriate model**:
   - Daily use: `gemini-2.5-flash` (fast)
   - High-quality translation: `gemini-2.5-pro` (high quality)

2. **Utilize caching mechanism**:
   - Keep cache files to support resume capability
   - Same content won't be translated repeatedly

3. **Batch processing**:
   - Use directory batch translation for improved efficiency
   - Use `--quiet` mode to reduce output overhead

## License

This project is open-sourced under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit Issues and Pull Requests to improve this tool. Particularly welcome contributions in the following areas:
- New text extraction algorithm optimizations
- More language support
- Performance improvement suggestions
- Error handling enhancements

---

*This repository files are generated by [Cursor](https://cursor.sh/) AI assistant* 
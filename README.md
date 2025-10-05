# TDS CI Caching Demo

This repository demonstrates advanced GitHub Actions caching with `actions/cache@v4`.

## Features

- ✅ **Python dependency caching** with pip cache
- ✅ **Custom cache key**: `cache-ab1694b` 
- ✅ **Cache hit/miss detection** in `prime-cache-ab1694b` step
- ✅ **Multi-job cache validation**
- ✅ **Comprehensive cache statistics**

## Workflow Details

The GitHub Actions workflow (`.github/workflows/ci-with-caching.yml`) includes:

1. **Dependency Caching**: Caches `~/.cache/pip` and installed packages
2. **Cache Key**: `cache-ab1694b-{OS}-python-3.11-{requirements-hash}`
3. **Prime Cache Step**: Echoes cache hit/miss status
4. **Cache Validation**: Second job tests cache restoration


## Expected Behavior

- **First Run**: Cache MISS → Install dependencies → Populate cache
- **Subsequent Runs**: Cache HIT → Skip installation → Faster builds

## Dependencies

See `requirements.txt` for cached packages:
- requests
- pandas  
- pytest
- fastapi
- uvicorn

## Testing

The workflow automatically:
1. Detects cache status
2. Installs dependencies only on cache miss
3. Validates package availability
4. Reports cache statistics

# 🔐 Security Configuration for LibraryProject

## HTTPS & Redirects
- `SECURE_SSL_REDIRECT = True`: Forces HTTPS.
- `SECURE_HSTS_SECONDS = 31536000`: Enables HSTS for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`: Applies to subdomains.
- `SECURE_HSTS_PRELOAD = True`: Allows preload list inclusion.

## Secure Cookies
- `SESSION_COOKIE_SECURE = True`: Session cookies sent only over HTTPS.
- `CSRF_COOKIE_SECURE = True`: CSRF tokens sent only over HTTPS.

## Security Headers
- `X_FRAME_OPTIONS = "DENY"`: Prevents clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents MIME-type sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Helps prevent XSS.

## Deployment Notes
- Use **Let’s Encrypt** for free SSL certificates.
- Ensure web server (Nginx/Apache) is configured for HTTPS.
- Always set `DEBUG = False` in production.

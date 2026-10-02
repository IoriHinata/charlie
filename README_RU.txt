CHARLIE — Android WebView без HTTP-сервера

Что внутри:
- app/src/main/assets/index.html — интерфейс HTML;
- app/src/main/assets/charlie.py — Python-мозг, загружается автоматически;
- Android WebViewAssetLoader — открывает локальные ресурсы через внутренний HTTPS-origin appassets.androidplatform.net, без запуска веб-сервера;
- системные разрешения CAMERA и RECORD_AUDIO запрашиваются Android, когда страница включает сенсоры;
- интернет остаётся доступен для Pyodide CDN и русской Википедии.

Сборка через GitHub Actions:
1. Распакуйте архив.
2. Загрузите ВСЕ файлы и папки проекта в корень репозитория GitHub, сохраняя структуру.
3. Откройте вкладку Actions.
4. Выберите “Build CHARLIE APK”.
5. Нажмите “Run workflow”.
6. После завершения откройте запуск и скачайте artifact “CHARLIE-debug-apk”.
7. Распакуйте artifact ZIP и установите app-debug.apk на Android.

Первый запуск требует интернета для загрузки Pyodide и NumPy. Сам интерфейс и charlie.py находятся внутри APK. Доступ к камере/микрофону разрешите в системном диалоге Android.

Если Actions завершится ошибкой, пришлите красный блок ошибки из конца лога.

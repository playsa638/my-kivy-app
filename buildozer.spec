[app]
title = 記帳小幫手
package.name = jizhangapp
package.domain = org.example.jizhang
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pandas,matplotlib,openpyxl,requests
entrypoint = main.py
orientation = portrait
fullscreen = 1
icon.filename = %(source.dir)s/icon.png
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.hide_statusbar = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.ndk = 25b
android.arch = armeabi-v7a
android.minapi = 21
android.allow_backup = 1
android.use_androidx = 1
[app]

# (str) Title of your application
title = Consultor Medica IA

# (str) Package name
package.name = consultormedicaia

# (str) Package domain (needed for android packaging)
package.domain = org.ia

# (str) Source files where the let it go (relative to directory of buildozer.spec)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (str) Directorate where the source code is stored
source.dir = .

# (list) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd,requests,urllib3,certifi,charset-normalizer,idna

# (list) Supported orientations
orientation = portrait

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minimum_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Automatically accept the Android SDK license
android.accept_sdk_license = True

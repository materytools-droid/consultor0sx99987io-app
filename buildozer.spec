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

# (list) Source files to omit (relative to directory of buildozer.spec)
#source.exclude_exts = spec

# (list) List of directory to omit (relative to directory of buildozer.spec)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,requests,urllib3,certifi,charset-normalizer,idna

# (list) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
#services = NAME:gs://path/to/script,NAME2:gs://path/to/script

#
# OSX Specific
#

#
# Number of CPU to use for parallel compilation
#osx.cpu_count = 4

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Features
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minimum_api = 21

# (str) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API version to use.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
#android.app_activity = org.kivy.android.PythonActivity

# (str) Supported orientations: landscape, sensorLandscape, portrait or fullSensor
#orientation = portrait

# (list) The Android archs to build for,, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enable Android auto backup
#android.allow_backup = True

# (str) XML files to include in the Manifest android:resource section
#android.manifest_application_xml =

# (str) Extra xml to include in <application> tag
#android.manifest_application_ext_xml =

# (str) Extra xml to include in <manifest> tag
#android.manifest_ext_xml =

# (str) Extra xml to include in <activity> tag
#android.manifest_activity_ext_xml =

# (str) Extra python-for-android build options
#p4a.build_options = --use-sdcard=private

# (bool) Automatically accept the Android SDK license
android.accept_sdk_license = True

[app]

title = Math Work

package.name = mathwork

package.domain = org.mathwork

source.dir = .

source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

icon.filename = %(source.dir)s/icon.png

android.accept_sdk_license = True

android.api = 33

android.minapi = 24

android.ndk = 28c

android.archs = arm64-v8a,armeabi-v7a


[buildozer]

log_level = 2

warn_on_root = 1

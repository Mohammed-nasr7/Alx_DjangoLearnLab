## تخصيص واجهة Django Admin لنموذج Book

### الخطوات:

1. تم تسجيل نموذج Book في ملف `admin.py` لتمكين إدارة الكتب من خلال **Django Admin**:
   ```python
   from django.contrib import admin
   from .models import Book
   admin.site.register(Book)

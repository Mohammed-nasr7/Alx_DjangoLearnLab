

## الأذونات المخصصة:
- **can_view**: 
- **can_create**:
- **can_edit**:
- **can_delete**:

## المجموعات:
- **Viewers**: يتم تعيين إذن `can_view`.
- **Editors**: يتم تعيين الأذونات `can_view`, `can_create`, `can_edit`.
- **Admins**: يتم تعيين الأذونات `can_view`, `can_create`, `can_edit`, `can_delete`.

## (Views):
- **view_article**: يحتاج إلى إذن `can_view`.
- **create_article**: يحتاج إلى إذن `can_create`.
- **edit_article**: يحتاج إلى إذن `can_edit`.
- **delete_article**: يحتاج إلى إذن `can_delete`.

## كيفية الاختبار:
1. إنشاء مستخدمين
2. تسجيل الدخول كمستخدم

# aepp
Django project

Если ваш JavaScript код находится в файлах статики (static files), вы можете использовать data-атрибуты для передачи данных из Django шаблона в JavaScript.

Пример:

```html
<!-- my_template.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Template</title>
    <script>
        var myVariable = "{{ my_variable }}";
        document.documentElement.setAttribute('data-my-variable', myVariable);
    </script>
    <script src="{% static 'js/my_script.js' %}"></script>
</head>
<body>
    <!-- Ваш HTML контент здесь -->
</body>
</html>
```

```javascript
// my_script.js
document.addEventListener('DOMContentLoaded', function() {
    var myVariable = document.documentElement.getAttribute('data-my-variable');
    console.log(myVariable);  // Вы можете использовать переменную myVariable в вашем JavaScript коде
});
```

В этом примере значение переменной `my_variable` передается из Django шаблона в JavaScript код через data-атрибут узла `documentElement`. JavaScript файл `{% static 'js/my_script.js' %}` будет иметь доступ к этому значению, когда страница загрузится.  
# friend_service

friends_serv

Все делается из корневой директории проекта:

    Установить все зависимости из requirements.txt - pip install -r requirements.txt;
    Запустить сервер с помощью команды - python manage.py runserver;
    Эндпоинты (спецификация) описаны в файле specification.yml в корне проекта.
    
    
    - При регистрации пользователя по адресу http://127.0.0.1:8000/auth/register/ проходим стандартную процедуру регистрации. Вводим логин, пароль и еще раз пароль. Пользователь сразу оказывается в системе.
    - Отправка запроса в друзья осуществляется по адресу http://127.0.0.1:8000/friends/send-request/<int:user_id>/. Создается исходящий запрос у текущего пользователя и входящий у получателя.
    - Принять запрос в друзья: http://127.0.0.1:8000/friends/accept-request/<int:request_id>/.
    - Отклонить запрос в друзья: http://127.0.0.1:8000/friends/reject-request/<int:request_id>/.
    - Узнать статус запроса: http://127.0.0.1:8000/friends/request-status/<int:user_id>/.
    - Список друзей пользователя можно отобразить по этой ссылке http://127.0.0.1:8000/friends/friendslist/.
    - Удалить друга: http://127.0.0.1:8000/friends/delete-friend/<int:user_id>/.
    - Список заявок пользователя можно отобразить по этой ссылке http://127.0.0.1:8000/friends/requestlist/.
    

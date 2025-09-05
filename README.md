
Основная концепция заключается в наличии смарт-устройства, которое содержит в себе "секрет" для криптографического алгоритма и сам алгоритм генерации ключей. "Секрет" с устройства нельзя считать обычными способами. При создании у каждой карты есть время жизни. Изначально "секрет" оказывается на карте при заполнении карты в режиме администрирования (ещё на карте есть id владельца, для обращения в БД). Так же этот "секрет" хранится в базе данных на сервере. На карте генерируется случайный набор байтов фиксированный длины при контакте со считывателем, который является необходимой частью для генерации пароля, при считывании этот набор передаётся на сервер вместе с паролем и id пользователя, там при помощи этого набора байтов и секрета из БД снова генерерируется пароль по тому же алгоритму. При всех корретных обстоятельствах при считывании смарт-устройства и обращении к базе данных, создаваемые ключи совпадают, и владелец смарт-устройства получает доступ.
[Итоги по кейсу_кт3.pdf](https://github.com/user-attachments/files/22169370/_.3.pdf)
![Untitled](https://github.com/user-attachments/assets/910bc7fc-2d8d-4f5a-b526-8bdd09bcff7b)



2 КТ: На данном этапе реализованы база данных, API базы данных, API сервера, API reader'а(эмуляция отправки сигнала на сервер), криптографический алгоритм для создания ключей, процесс аутенфикации, веб-интерфейс админ-панели. Реализовано 60%. Всё было реализовано в виде микросервисной архитектуры(разделено по docker-контейнерам). В планах: создание и реализация эмуляторов карты и reader'а, а также функционал админ-панели.

<img width="1280" height="496" alt="image" src="https://github.com/user-attachments/assets/c10c5bdb-bf98-4ea5-a1a2-196d30192ca2" />

<img width="1584" height="897" alt="image" src="https://github.com/user-attachments/assets/66438171-ee92-4beb-93bf-809bbfce1ae7" />

<img width="1576" height="479" alt="image" src="https://github.com/user-attachments/assets/10f1ddaf-2354-482b-befa-d9706e9efe9a" />

<img width="1534" height="823" alt="image" src="https://github.com/user-attachments/assets/88c14690-0b25-4e46-93f6-13f7fc3c6e42" />

 <img width="1423" height="855" alt="image" src="https://github.com/user-attachments/assets/39894a36-fb38-47ad-8daf-9f2f2e0475a9" />

 <img width="1352" height="382" alt="image" src="https://github.com/user-attachments/assets/6b07ee2e-5ea3-4910-b7f1-de1b777117c5" />

<img width="1811" height="703" alt="image" src="https://github.com/user-attachments/assets/b9152999-4142-497e-a8e8-989e1252087c" />

<img width="560" height="837" alt="image" src="https://github.com/user-attachments/assets/2c19a3de-3380-45b7-b30e-483aa2edace6" />

<img width="1584" height="897" alt="image" src="https://github.com/user-attachments/assets/c8ab0e4e-f858-4622-91fb-ecfdaa6df2eb" />


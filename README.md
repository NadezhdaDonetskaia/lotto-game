## **Lotto-game**
This is the well known lotto game.
You play with the computer with 1 card each.

### Description
+ If you crossed out all the numbers on the card before the computer - you won!!!
+ If you did not notice on the card and did not cross out the dropped number - you lost :(

### How to install

```
docker build -t myapp .
```

### How to play

```
docker run -it myapp
```

### Levels
    0 - самый простой, у тебя неогранниченное время на ответ (по умолчанию)   
    1 - посложнее, у тебя 30 секунд на ответ   
    2 - средний, 10 секунд на ответ   
    3 - сложный, время на ответ будет сокращаться вместе с числами в карточке



### Codeclimate
[![Maintainability](https://api.codeclimate.com/v1/badges/a544dba7e1007c7c63b3/maintainability)](https://codeclimate.com/github/Nella611/lotto-game/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/a544dba7e1007c7c63b3/test_coverage)](https://codeclimate.com/github/Nella611/lotto-game/test_coverage)
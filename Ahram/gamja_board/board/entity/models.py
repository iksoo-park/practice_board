from django.db import models

# Create your models here.

class Board(models.Model):
    boardId = models.AutoField(primary_key=True)
    boardName = models.CharField(max_length=32, null=False)
    boardContext = models.TextField()
    boardWriter = models.CharField(max_length=32, null=False)
    regDate = models.DateTimeField(auto_now_add=True)
    updDate = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"boardId: {self.boardId}, boardName: {self.boardName}"
        # 디버깅 용도
        # print를 했을 때 이렇게 출력하겠다


    class Meta:
        db_table = 'board'





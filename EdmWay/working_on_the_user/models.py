from django.db import models

class Traks(models.Model):

    name = models.CharField(
        max_length = 50, 
        verbose_name = "Название")    
    performer = models.CharField(
        max_length = 20, 
        verbose_name = "Исполнитель")
    album = models.CharField(
        max_length = 20, 
        verbose_name = "Альбом")
    date_relised =  models.CharField(
        max_length = 20, 
        verbose_name = "Дата выхода")
    trak = models.FileField(
        upload_to = 'uploads/%Y/%m/%d/',
        verbose_name = "file")

    def __str__(self) -> str:
        return self.name

    class Meta:
        """
        How it will be displayed in the django admin panel
        """
        verbose_name = "Трек"
        verbose_name_plural = "Треки"
    

class Comments(models.Model):

    text_comment = models.CharField(
        max_length = 300, 
        verbose_name = "Текст комментария")
    user_name = models.CharField(
        max_length = 30, 
        verbose_name = "Ник пользователя")
    name_track = models.CharField(
        max_length = 30, 
        verbose_name = "Под каким треком")
    
    def __str__(self) -> str:
        return self.id

    class Meta:
        """
        How it will be displayed in the django admin panel
        """
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

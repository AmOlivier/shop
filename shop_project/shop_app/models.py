from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=264)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(default="static/images/ecran.png", upload_to='static/images/' )

    def __str__(self):
        return (self.name)

    # def __repr__(self):
    #     return "<Product {}>".format(self.name)



class Client(models.Model):
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	password = models.CharField(max_length=50)
	email = models.EmailField()
	profil_picture = models.ImageField(default="static/images/profil_pictures/defaultpicture.jpg", upload_to='static/images/profil_pictures/' )



	def __str__(self):
		return self.first_name

	def __repr__(self):
		return "<Client {}>".format(self.email)

class Maillot(models.Model):
	name = models.CharField(max_length=264)
	description = models.TextField()
	price = models.DecimalField(max_digits=5, decimal_places=2)
	maillot_picture = models.ImageField(default="static/images/maillots_pictures/maillotdefaut.jpg", upload_to='static/images/maillots_pictures/' )


	def __str__(self):
		return self.name

	
	def __repr__(self):
		return "<Client {}>".format(self.name)

class Comment(models.Model):
	username = models.CharField(max_length=264)
	text = models.TextField()
	date = models.DateField()
	product = models.ForeignKey(Product , on_delete=models.CASCADE)


	def __str__(self):
		return self.username

	
	def __repr__(self):
		return "<Client {}>".format(self.username)


		


# class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100 **options)

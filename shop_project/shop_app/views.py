from django.shortcuts import render ,redirect
from shop_app.models import Product , Client, Maillot, Comment, Question, Response, CommentResponse
from shop_app.forms import CommentForm, QuestionForm, ResponseForm, CommentResponseForm
import datetime 

# Create your views here.
def index(request):
   products = Product.objects.all()[:20]
   return render(request,"index.html",context={'products':products})

def product(request, product_id):
  product = Product.objects.get(id=product_id)
  comments = Comment.objects.all().filter(product_id=product_id)

  comments_with_responses = []
  for comment in comments:
    comment_with_responses = {
      'comment': comment,
      'commentresponses': CommentResponse.objects.all().filter(comment_id=comment.id)
    }

    comments_with_responses.append(comment_with_responses)



  questions = Question.objects.all().filter(product_id=product_id)

  questions_with_responses = []
  for question in questions:
    question_with_responses = {
      'question': question,
      'responses': Response.objects.all().filter(question_id=question.id)
    }

    questions_with_responses.append(question_with_responses)

  return render(request, 'product.html', context={
      'product': product,
      'questions': questions_with_responses,
      'comments': comments_with_responses,
    })

def clients(request):
	clients = Client.objects.all()[:20]
	return render(request, "clients.html", context={'clients': clients })

def client(request, client_id):
	client = Client.objects.get(id=client_id)
	return render(request, "client.html", context={'client': client })

def maillots(request):
	maillots = Maillot.objects.all()
	return render(request, "maillots.html", context={'maillots': maillots })

def maillot(request, maillot_id):
	maillot = Maillot.objects.get(id=maillot_id)
	return render(request, "maillot.html", context={'maillot': maillot })

def comment_form(request, product_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		product = Product.objects.get(id=product_id)
		date = datetime.datetime.now()
		Comment.objects.get_or_create(username=username,text=text,date=date,product=product)
	

	
	comment_form = CommentForm()
	return render(request, "comment_form.html", context={'comment_form': comment_form })



def question_form(request, product_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		title = request.POST.get('title')
		text = request.POST.get('text')
		product = Product.objects.get(id=product_id)
		Question.objects.get_or_create(username= username,title=title,text=text,product=product)

		return redirect('/shop_app/products/{}/'.format(product_id))


	return render(request, "question_form.html", context={'question_form': QuestionForm()})


def responseform(request, question_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		question = Question.objects.get(id=question_id)
		Response.objects.get_or_create(username= username,text=text,question=question)

		return redirect('/shop_app/products/{}/'.format(question.product.id))


	return render(request, "responseform.html", context={'responseform': ResponseForm()})


def commentresponseform(request, comment_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		comment = Comment.objects.get(id=comment_id)
		CommentResponse.objects.get_or_create(username= username,text=text,comment=comment)

		return redirect('/shop_app/products/{}/'.format(comment.product.id))


	return render(request, "commentresponseform.html", context={'commentresponseform': CommentResponseForm()})

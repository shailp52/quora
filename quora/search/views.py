from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from quora.questions.models import Question
from django.contrib.auth.decorators import login_required
from quora.core.redis_cache import RedisCache


redis = RedisCache()
REDIS_SEARCH_KEY = "SEARCH|{}"

def search(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()
        if len(querystring) == 0:
            return redirect('/search/')
        # import ipdb; ipdb.set_trace()
        results = redis.get_pickle(REDIS_SEARCH_KEY.format(querystring))
        if results:
            return render(request, 'search/results.html', {
                'querystring': querystring,
                'results': results
            })
        
        search_type = 'questions'

        count = {}
        results = {}

        results['questions'] = Question.objects.filter(Q(title__icontains=querystring) | Q(content__icontains=querystring))
        count['questions'] = results['questions'].count()
        redis.save_pickle(key=REDIS_SEARCH_KEY.format(querystring), data=results['questions'], ex=60 * 60 * 1000) # 1 hour expiry
        return render(request, 'search/results.html', {
            'querystring': querystring,
            'results': results['questions']})
    else:
        return render(request, 'search/search.html', { 'hide_search': True })

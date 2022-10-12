@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(), pk=user_pk)
        me = request.user

        if you != me:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
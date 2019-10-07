def get_user_from_request(request):
    # TODO Add Error Handling if the user is not logged in.
    return request.user

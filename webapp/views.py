from django.shortcuts import render


class Views:

    @staticmethod
    def home_view(request):
        return render(request, 'index.html')

    @staticmethod
    def one_view(request):
        name = "First Page"
        body = ('"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt'
                ' ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco'
                ' laboris nisi ut aliquip ex ea commodo consequat."')

        return render(request, 'page.html', context={'name': name, 'body': body})

    @staticmethod
    def two_view(request):
        name = "Second Page"
        body = ('"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque '
                'laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto '
                'beatae vitae dicta sunt explicabo."')

        return render(request, 'page.html', context={'name': name, 'body': body})

    @staticmethod
    def three_view(request):
        name = "Third Page"
        body = ('"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum '
                'deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non '
                'similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga."')

        return render(request, 'page.html', context={'name': name, 'body': body})

    @staticmethod
    def four_view(request):
        name = "Fourth Page"
        body = (
            '"Morbi varius ornare eros, ullamcorper condimentum nunc venenatis eget. Ut interdum ex mattis metus '
            'posuere varius. Vivamus varius iaculis elit. Nunc scelerisque nisi eu interdum viverra. Fusce scelerisque,'
            ' purus sed elementum imperdiet, orci turpis sollicitudin metus, vel imperdiet mauris tortor et orci."')

        return render(request, 'page.html', context={'name': name, 'body': body})

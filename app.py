from flask import Flask, render_template

app = Flask(__name__)


# TODO: Restaurant List of Dictionaries
# image_url, restaurant_name, status, location, id
restaurants = [
    {
        "id": 1,
        "location": "Makati",
        "restaurant_name": "Restaurant One",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 2,
        "location": "Pasig",
        "restaurant_name": "Restaurant Two",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/25858122/pexels-photo-25858122/free-photo-of-patio-of-cafe.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 3,
        "location": "Mandaluyong",
        "restaurant_name": "Restaurant Three",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/16550341/pexels-photo-16550341/free-photo-of-facade-of-urban-building.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 4,
        "location": "Quezon CIty",
        "restaurant_name": "Restaurant Four",
        "status": "Open",
        "image_url": "https://images.pexels.com/photos/12935080/pexels-photo-12935080.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 5,
        "location": "Alabang",
        "restaurant_name": "Restaurant Five",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/8921562/pexels-photo-8921562.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
    },
    {
        "id": 6,
        "location": "Pasig",
        "restaurant_name": "Restaurant Six",
        "status": "Closed",
        "image_url": "https://images.pexels.com/photos/14646764/pexels-photo-14646764.jpeg?auto=compress&cs=tinysrgb&w=600&lazy=load"
    },
    {
        "id": 7,
        "location": "Davao City",
        "restaurant_name": "Restaurant Seven",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/5e/04/d1/breakfast-set-up.jpg?w=1400&h=-1&s=1",
    },
    {
        "id": 8,
        "location": "Cebu City",
        "restaurant_name": "Restaurant Eight",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2d/13/b1/91/caption.jpg?w=1100&h=-1&s=1",
    },
    {
        "id": 9,
        "location": "Manila",
        "restaurant_name": "Restaurant Nine",
        "status": "Closed",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/33/10/3e/manila-bay-kitchen-is.jpg?w=1400&h=-1&s=1",
    },
    {
        "id": 10,
        "location": "Ilagan",
        "restaurant_name": "Restaurant Ten",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/47/52/2d/the-borough-pizza-pub.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 11,
        "location": "Palayan City",
        "restaurant_name": "Restaurant Eleven",
        "status": "Open",
        "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/vw2pstkK9LIM4Mg66lu-qw/o.jpg",
    },
    {
        "id": 12,
        "location": "Quezon City",
        "restaurant_name": "Restaurant Twelve",
        "status": "Closed",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/16/c7/47/4a/seven-corners-restaurant.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 13,
        "location": "Cavite City",
        "restaurant_name": "Restaurant Thirteen",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/77/b3/73/mozu-at-ming-s.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 14,
        "location": "Baguio",
        "restaurant_name": "Restaurant Fourteen",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/21/9e/28/81/always-a-feast.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 15,
        "location": "Antipolo",
        "restaurant_name": "Restaurant Fifteen",
        "status": "Closed",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/39/0c/03/caption.jpg?w=1100&h=600&s=1",
    },
    {
        "id": 16,
        "location": "Pasig",
        "restaurant_name": "Restaurant Sixteen",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/b7/30/68/kalesa-cafe-bar-area.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 17,
        "location": "Pasay",
        "restaurant_name": "Restaurant Seventeen",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/ee/07/78/china-blue-by-jereme.jpg?w=1100&h=600&s=1",
    },
    {
        "id": 18,
        "location": "Cagayan de Oro",
        "restaurant_name": "Restaurant Eighteen",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/b6/b8/46/mindanao-heritage-cuisine.jpg?w=1000&h=600&s=1",
    },
    {
        "id": 19,
        "location": "Angeles",
        "restaurant_name": "Restaurant Nineteen",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/fa/62/6f/monster-board.jpg?w=1000&h=600&s=1",
    },
    {
        "id": 20,
        "location": "Zamboanga",
        "restaurant_name": "Restaurant Twenty",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0b/e7/48/50/fb-img-1468066408696.jpg?w=600&h=500&s=1",
    },
    {
        "id": 21,
        "location": "Bayugan City",
        "restaurant_name": "Restaurant Twenty One",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/42/a6/f0/view-from-cafe-de-jardin.jpg?w=1600&h=900&s=1",
    },
    {
        "id": 22,
        "location": "Himamaylan City",
        "restaurant_name": "Restaurant Twenty Two",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/09/5b/8c/a9/some-beverages-on-offer.jpg?w=1600&h=900&s=1",
    },
    {
        "id": 23,
        "location": "Lamitan City",
        "restaurant_name": "Restaurant Twenty Three",
        "status": "Open",
        "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/ViEbEK_fyWvd8PaiOCQGmA/l.jpg",
    },
    {
        "id": 24,
        "location": "Calbayog City",
        "restaurant_name": "Restaurant Twenty Four",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/a7/9a/68/crispy-shrimps.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 25,
        "location": "Borongan City",
        "restaurant_name": "Restaurant Twenty Five",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/23/60/e2/32/mango-mud-pie.jpg?w=1100&h=600&s=1",
    },
    {
        "id": 26,
        "location": "Taguig City",
        "restaurant_name": "Restaurant Twenty Six",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/9d/30/65/the-dining-room.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 27,
        "location": "Caloocan",
        "restaurant_name": "Restaurant Twenty Seven",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2d/9b/57/56/caption.jpg?w=1100&h=600&s=1",
    },
    {
        "id": 28,
        "location": "San Juan City",
        "restaurant_name": "Restaurant Twenty Eight",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/08/a9/bc/0a/the-food.jpg?w=1600&h=900&s=1",
    },
    {
        "id": 29,
        "location": "Laoag",
        "restaurant_name": "Restaurant Twenty Nine",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/92/59/b7/taste-ilocano-food.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 30,
        "location": "El Salvador City",
        "restaurant_name": "Restaurant Thirty ",
        "status": "Close",
        "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/9l7piq9U5fvTf-BfwPrrXg/l.jpg",
    },
    {
        "id": 31,
        "location": "Legazpi City",
        "restaurant_name": "Restaurant Thirty One",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/e3/15/61/caption.jpg?w=1100&h=600&s=1",
    },
    {
        "id": 32,
        "location": "Basilan",
        "restaurant_name": "Restaurant Thirty Two",
        "status": "Open",
        "image_url": "data:image/jpeg;base64,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"    },
    {
        "id": 33,
        "location": "Vigan City",
        "restaurant_name": "Restaurant Thirty Three",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/35/8f/32/1995-studio-cafe.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 34,
        "location": "Talisay",
        "restaurant_name": "Restaurant Thirty Four",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/b7/e3/cb/20190803-101732-largejpg.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 35,
        "location": "Carcar",
        "restaurant_name": "Restaurant Thirty Five",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/66/3f/f2/photo0jpg.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 36,
        "location": "Dumaguete",
        "restaurant_name": "Restaurant Thirty Six",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/21/e2/bb/c4/buglas-isla-is-a-casual.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 37,
        "location": "Mabalacat",
        "restaurant_name": "Restaurant Thirty Seven",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2d/53/19/eb/experience-the-best-of.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 38,
        "location": "Bais City",
        "restaurant_name": "Restaurant Thirty Eight",
        "status": "Open",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHe2b81i-Es0rgywtc3xaT2Jvfk1XWiuWb7Q&s",
    },
    {
        "id": 39,
        "location": "Tagbilaran City",
        "restaurant_name": "Restaurant Thirty Nine",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/19/5b/d7/8b/le-panorama-restaurant.jpg?w=1200&h=700&s=1",
    },
    {
        "id": 40,
        "location": "Tagaytay",
        "restaurant_name": "Restaurant Forty",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/29/f7/87/78/caption.jpg?w=1100&h=600&s=1",
    },
    {
        "id": 41,
        "location": "Danao City",
        "restaurant_name": "Restaurant Forty One",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/37/5d/64/20190810-135308-largejpg.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 42,
        "location": "San Fernando City",
        "restaurant_name": "Restaurant Forty Two",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/9d/e8/a8/stage-set-up-credits.jpg?w=1000&h=600&s=1",
    },
    {
        "id": 43,
        "location": "San Pedro",
        "restaurant_name": "Restaurant Forty Three",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/13/ff/12/4a/mixed-buttered-shrimp.jpg?w=1000&h=600&s=1",
    },
    {
        "id": 44,
        "location": "Lucena City",
        "restaurant_name": "Restaurant Forty Four",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/07/ae/eb/43/sadik-resto-bar.jpg?w=1600&h=-1&s=1",
    },
    {
        "id": 45,
        "location": "San Pablo",
        "restaurant_name": "Restaurant Forty Five",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/17/28/72/13/photo9jpg.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 46,
        "location": "Bacoor",
        "restaurant_name": "Restaurant Forty Six",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/28/e7/c3/tong-yang-plus-sm-city.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 47,
        "location": "Cotabato City",
        "restaurant_name": "Restaurant Forty Seven",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/1a/5e/a9/photo2jpg.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 48,
        "location": "San Carlos City",
        "restaurant_name": "Restaurant Forty Eight",
        "status": "Close",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/4f/e9/95/photo3jpg.jpg?w=1400&h=800&s=1",
    },
    {
        "id": 49,
        "location": "Cauayan City",
        "restaurant_name": "Restaurant Forty Nine",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2a/c3/98/cc/fine-dining-multicuisine.jpg?w=1100&h=600&s=1",
    },
    {
        "id": 50,
        "location": "Naga",
        "restaurant_name": "Restaurant Fifty ",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2b/9a/9c/0e/quality-filipino-mediterranean.jpg?w=1400&h=800&s=1",
    }
]


@app.route('/')
def hello_world():
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)
var selections = {
    "East Campus": {
        "Breadwinners- Questrom": {
            "Breakfast Sides" : ["Strawberry Yogurt Parfait", "Mixed Fruit Cup", "Chobani Yogurt"],
            "Daily Pastries" : ["Apple Turnover", "Apple Danish", "Raspberry Danish", "Apple Muffin", "Chocolate Chip Muffin", "Blueberry Muffin", "Cinnamon Roll", "Cinnamon Swirl Crumb Cake"],
            "Desserts": ["Chewy Marshmallow bar w/ Brown Butter & Sea Salt", "Totally Oreo Brownie", "Chocolate Peanut Butter Snack", "Summerberry Stack", "Toffee Crunch Blondie", "Fabulous Chocolate Chunk Brownie", "Lemon Crumb Bar", "David's Chocolate Chip Cookie"],
            "Soups": ["Pasta E Fagioli", "Creamy Tomato Soup"],
            "Daily Specials": ["Teriyaki Salmon with Lemon Green Beans, Brown Rice Quinoa Blend", "Crispy Five Spice Tofu, Quinoa and Wild Rice Blend", "Chicken and Vegetable Lo Mein", "Tofu and Vegetable Lo Mein", "Yucatan Bowl", "Grill Vegetables Yucatan Bowl", "Sesame Chicken with Fried Rice", "Crispy Sesame Tofu with Fried Rice", "Grilled Herbed Salmon w/ Lemon Burre Blanc Sauce, Steamed Rice & Green Beans", "Grilled Tofu w/ Lemon Burre Blanc Sauce, Steamed Rice & Green Beans", "Baked Orange Ginger Salmon, Jasmine Rice, and Steamed Broccoli", "General Tso's Vegan Beef, Jasmine Rice, and Steamed Broccoli", "Arroz Con Pollo /w Plantains", "Grilled Zucchini & Red Pepper, Rice w/ Plantains", "Jerk Chicken with Rice and Beans", "Jerk Tofy with Rice and Beans"]
        },
        "Starbucks": {
            "Featured Beverages": ["Pistachio Latte", "Iced Pistachio Latte", "Pistachio Cream Cold Brew", "Pistachio Creme", "Pistachio Coffee Frappuccino Blended Beverage", "Pistachio Creme Frappuchino Blended Beverage", "Lavender Oatmilk Chill", "Spicy Pineapple Passionfruit Lemonade Starbucks Refreshers", "Spicy Strawberry Acai Lemonade Starbucks Refreshers Beverage", "Spicy Mango Dragonfruit Lemonade Starbucks Refreshers Beverages", "Iced Lavender Cream Oatmilk Matcha", "Iced Lavender Oatmilk Latte", "Lavender Creme Frappuchino Blended Beverage"],
            "Oleato": ["Oleato Caffe Latte with Oatmilk", "Iced Chai Tea Latte with Oleato Golden Foam", "Oleato Iced Shaken Espresso with Oatmilk and Toffeenut", "Dragon Drink Starbucks Refreshers Beverage with Oleato Golden Foam", "Paradise Drink Starbucks Refreshers Beverage with Oleato Golden Foam", "Iced Matcha Tea Latte with Oleato Golden Foam"],
            "Featured Food": ["Vanilla Bean Custard Danish", "Pumpkin & Pepita Loaf"],
            "Coffee, Tea & More": ["Freshly Brewed Coffee", "Caffe Misto", "Matcha Green Tea Latte", "London Fog Tea Latte", "Royal English Breakfast Tea Latte", "Chai Latte", "Teavana Brewed Tea", "Honey Citrus Mint Tea", "White Hot Chocolate", "Hot Chocolate", "Caramel Apple Spice", "Syrup Creme"],
            "Iced Coffee, Tea & More": ["Iced Coffee", "Cold Brew Coffee", "Vanilla Sweet Cream Cold Brew", "Salted Caramel Cream Cold Brew", "Cinnamon Caramel Cream Cold Brew", "Chocolate Cream Cold Brew", "Iced Chai Latte", "Iced Matcha Grean Tea Latte", "Teavana Shaken Iced Tea", "Teavana Shaken Iced Tea Lemonade", "Iced Peach Green Tea", "Iced Peach Green Tea Lemonade", "Iced Shaken Matcha Lemonade", "Lemonade"],
            "Hot Espresso Beverages": ["Espresso", "Espresso Macchiato", "Caffe Americano", "Flat White", "Caffe Latte", "Caffe Mocha", "White Chocolate Mocha", "Caramel Macchiato", "Cinnamon Dolce Latte", "Cappuchino"],
            "Iced Espresso Beverages": ["Espresso Over Ice", "Iced Caffe Americano", "Iced Caffe Latte", "Iced Caramel Macchiato", "Iced Caffe Mocha", "Iced Flat White", "Iced White Chocolate Mocha", "Iced Cinnamon Dolce Latte", "Iced Cappuchino", "Iced Shaken Espresso", "Iced Brown Sugar Oatmilk Shaken Espresso", "Iced Hazelnut Oatmilk Shaken Espresso"],
            "Frappuchino": ["Coffee Frappuccino", "Caramel Frappuccino Blended Coffee", "Mocha Frappuchino Blended Coffee", "Strawberry Frappuchino", "Java Chip Frappuccino", "Vanilla Bean Creme Frappuccino", "Double Chocolaty Chip Creme Frappuccino", "Matcha Green Tea Creme Frappuccino", "White Chocolate Mocha Frappuccino Blended Coffee", "Caffe Vanilla Frappuccino Blended Coffee", "Chai Creme Frappuccino Blended Creme", "Mocha Cookie Crumble Frappuccino", "Caramel Ribbon Crunch Frappuccino"],
            "Starbucks Refreshers": ["Pineapple Passionfruit Starbucks Refreshers Beverage", "Mango Dragonfruit Starbucks Refreshers Beverage", "Strawberry Acai Starbucks Refreshers Beverage", "Paradise Drink Starbucks Refreshers Beverage", "Dragon Drink Starbucks Refreshers Beverage", "Pink Drink Starbucks Refreshers Beverage", "Mango Dragonfruit Refreshers Lemonade", "Strawberry Acai Refresher Lemonade", "Pineapple Passionfruit Lemonade Starbucks Refreshers Beverage", "Frozen Strawberry Acai Lemonade Starbucks Refreshers Beverage", "Frozen Mango Dragonfruit Lemonade Starbucks Refreshers Beverage", "Frozen Pineapple Passionfruit Lemonade Starbucks Refreshers Beverage"],
            "Breakfast": ["Bacon & Gruyere Sous Vide Egg Bites", "Egg White & Roasted Red Pepper Sous Vide Egg Bites", "Kale & Portabella Mushroom Sous Vide Egg Bites", "Impossible Breakfast Sandwich", "Double-Smoked Bacon, Cheddar & Egg Sandwich", "Bacon, Gouda & Egg Sandwich", "Sausage, Cheddar & Egg Sandwich", "Turkey Bacon, Cheddar & Egg White Breakfast Sandwich", "Bacon, Sausage & Egg Wrap", "Spinach, Feta & Egg White Wrap", "Rolled & Steel Cut Oatmeal"],
            "Sandwiches & Paninis": ["Turkey & Pesto Panini", "Tomato & Mozzarella", "Ham & Swiss Panini", "Crispy Grilled Cheese"],
            "Scones, Doughnuts, Danishes & Cakes": ["Cinnamon Coffee Cake", "Iced Lemon Pound Loaf", "Pumpkin Loaf", "Banana Nut Loaf", "Cheese Danish", "Glazed Doughnut", "Petite Vanilla Bean Scone", "Blueberry Scone"],
            "Cookies, Brownies, Cake Pops & Bars": ["Chocolate Chip Cookie", "Double Chocolate Brownie", "Chocolate Cake Pop", "Cookies & Cream Cake Pop", "Birthday Cake Pop"],
            "Croissants & Muffins": ["Blueberry Muffin", "Chocolate Croissant", "Butter Croissant", "Ham & Swiss Croissant"]
        },
        "Bay State Underground": {
            "Bay State Grill": ["Underground Burger", "Char-Grilled Burger", "Beyond Burger", "Crispy Chicken Sandiwch"],
            "Bay State Wraps & Salads": ["Caesar Salad", "Crispy Chicken Caesar Wrap", "Crispy Chicken Buffalo Caesar Wrap"],
            "Bay State Sweet Desserts": ["Cookies", "Cheesecakes", "Tiramisu Cake"]
            //check again when restocked
        },
        "Marciano's Dining Hall": {
            "Bakery": [],
            "Brick Oven": [],
            "Deli": [],
            "Gluten Free Kitchen": [],
            "Grill": [],
            "International": [],
            "Mediterranean": [],
            "Paseo": [],
            "Saute": [],
            "Vegan": []
        }
    },
    "Central Campus":{
        "Law School Cafe": {
            "Breakfast Sandwiches & Pastries": ["Sausage in Session Sausage Egg & Cheese with Fig Jam", "Bacon & Order Bacon Egg & Cheese with Avocado", "The Verdict Egg & Cheese Bagel with Basil, Pesto, Cheddar Cheese, Avocado and Sundried Tomato", "Bagel", "Chocolate Croissant", "Banana Bread", "Coffee Cake Cinnamon Loaf", "Plain Croissant", "Blueberry Loaf", "Home Made Large Chocolate Chip Cookie"],
            "Iced Teas": ["Iced Black Tea", "Iced Green Tea", "Wild Berry Hisbiscus Iced Tea", "Iced Tea Lemonade", "Fruit Tea Shaker", "Iced Chai Latte"],
            "Coffee & Espresso & Hot Chocolate": ["Peet's Decaf Coffee", "Peet's Coffee", "Americano", "Cappuccino", "Pumpkin Latte", "Caffe Latte", "Vanilla Latte", "Caramel Macchiato", "Caffe Mocha", "White Chocolate Mocha", "Hot Chocolate", "Iced Caffe Americano", "Espresso"],
            "Teas Non-Coffee": ["Black, Green or Herbal Tea", "Chai Latte"],
            "Cold Brew & Signature Beverage": ["Cold Brew", "Cold Brew Oat Latte", "The Black Tie", "Matcha Latte", "Iced Caffe Americano"],
            "Frappe Blended Beverages": ["Mocha Frappe", "Caramel Frappe", "Matcha Frappe"],
            "Yogurt, Fruit, Parfaits": ["Mixed Fruit Cup", "Grape Cup", "Strawberry Parfait", "Overnight Oats with Chia Seeds"]
        },
        "Einstein Bros Bagels": {
            "Bagels": ["Bagel", "Bagel with Shmear", "Bagel with Peanut Butter", "Bagel with PB&J", "Bagel with Jelly", "Bagel with Butter", "Avocado Toast"],
            "Classic Egg Sandwiches": ["Egg, Cheese & Bacon Sandwich", "Turkey Sausage & Cheddar Egg Sandwich", "Ham & Swiss Egg Sandwich", "Egg & Cheese Sandwich"],
            "Signature Sandwiches": ["Farmhouse Egg Sandwich", "Big Breakfast Burrito", "Garden Avocado", "All Nighter Sandwich"],
            "Egg White Sandwich": ["Bacon, Avocado & Tomato Egg White", "Sante Fe Egg White Sandwich"],
            "Deli Lunch": ["Nova Lox & Bagel", "Turkey B.A.T Sandwich", "Tasty Turkey Sandwich", "Avocado Veg Out"],
            "Deli Selects": ["Turkey & Cheddar Deli Sandwich", "Ham & Swiss Deli Sandwich", "Chicken Salad Deli Sandwich"],
            "Hot and Toasty": ["Pepperoni & Chicken Sandwich", "Pizza bagel", "Spicy Chicken Ciabatta Sandwich", "Veggie Melt on Diabatta", "Albuquerque Turkey Sandwich"],
            "Desserts": ["Muffin", "Chocolate Chip Cookie", "Chocolate Chunk Cookie Poppers", "Twice-Baked Hash Brown", "Strawberry & Cream Strudel", "Apple Pie Pastry", "Cinnamon Bliss Roll"],
            "Hot Drinks": ["Coffee to Go", "Hot Chocolate", "Fresh-Brewed Coffee", "Mocha", "Caramel Macchiato", "Latte", "Chai Tea Latte", "Americano", "Cappuccino", "Vanilla Latte", "Hot Tea"],
            "Cold Drinks": ["Cold Brew", "Vainlla Cream Cold Brew", "Caramel Cream Cold Brew", "Chocolate Cream Cold Brew", "Iced Mocha", "Iced Caramel Macchiato", "Iced Latte", "Iced Chai Tea latte", "Iced Vanilla Latte", "Iced Americano", "Iced Cappuccino", "Iced Tea", "Espresso"],
            "Frozen & Blended Drinks": ["Vanilla Cold Brew Shake", "Caramel Cold Brew Shake", "Chocolate Cold Brew Shake", "Coffee Free Chocolate Cold Brew Shake", "Coffee Free Caramel Cold Brew Shake", "Coffee Free Vanilla Cold Brew Shake", "Coffee Free Cold Brew Shake", "Strawberry Banana Smoothie"],
            "Grab & Go": ["Chicken & Bacon Caesar Wrap", "California Turkey Club Wrap"],
            "Grab & Go Drinks": ["Lemonade", "Blackberry Lemonade", "White Milk", "Chocolate Milk"]
        }
    }
}

window.onload = function(){
    const selectLocation = document.getElementById('location-names'),
    selectVendorName = document.getElementById('vendor-names'),
    selectCategory = document.getElementById('category-names'),
    selectItem = document.getElementById('item-names'),
    select = document.querySelectorAll('select')

    selectVendorName.disabled = true;
    selectCategory.disabled = true;
    selectItem.disabled = true;

    select.forEach(select => {
        if (select.disabled == true){
            select.style.cursor = "auto";
        }
    });

    for (let location in selections){
        //console.log(location);
        selectLocation.options[selectLocation.options.length] = new Option(location, location);    
    }

    selectLocation.onchange = (e) =>{
        selectVendorName.disabled = false;
        selectCategory.disabled = true;
        selectItem.disabled = true;

        selectVendorName.length = 1;
        selectCategory.length = 1;
        selectItem.length = 1;

        for (let vendor in selections[e.target.value]){
            selectVendorName.options[selectVendorName.options.length] = new Option(vendor, vendor);
        }
    }

    selectVendorName.onchange = (e) =>{
        selectCategory.disabled = false;
        selectItem.disabled = true;

        selectCategory.length = 1;
        selectItem.length = 1;

        for (let category in selections[selectLocation.value][e.target.value]){
            selectCategory.options[selectCategory.options.length] = new Option(category, category);
        }
    }

    selectCategory.onchange = (e) =>{
        selectItem.disabled = false;

        selectItem.length = 1;

        let items = selections[selectLocation.value][selectVendorName.value][e.target.value];
        
        for (let i=0; i < items.length; i++){
            selectItem.options[selectItem.options.length] = new Option(items[i], items[i])
        }
        
    }
}
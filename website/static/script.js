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
            "Iced Espresso Beverages": ["Espresso Over Ice", "Iced Caffe Americano", "Iced Caffe Latte", "Iced Caramel Macchiato", "Iced Caffe Mocha", "Iced Flat White", "Iced White Chocolate Mocha", "Iced Cinnamon Dolce Latte", "Iced Cappuchino", "Iced Shaken Espresso", "Iced Brown Sugar Oatmilk Shaken Espresso", "Iced Hazelnut Oatmilk Shaken Espresso"]
        }
    },
    "Central Campus":{
    
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
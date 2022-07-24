const selectType = document.querySelector('.onSelect');
var pt = document.getElementById('productType');

function getInput(el){
    const option = el.value;
    pt.value = option;
    if (option == 'Most Selling Collection'){
        selectType.style.display = 'block';
    }
    else{
        selectType.style.display = 'none';
    }
}


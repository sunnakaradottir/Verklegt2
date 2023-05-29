$(document).ready(function(){
    $('#search-btn').on( 'click',  function(e){
        e.preventDefault();
        let searchText = $('#search-box').val();
        console.log(searchText)
        $.ajax({
            url: '/?search_filter='+ searchText,
            type: 'GET',
            success: function(resp) {
                console.log(resp.data);
                let newHtml = resp.data.map(d => {
                    let priceHtml = d.price === null ? '0' : d.price;


                    return `<a class="single_item" href="/item/${d.id}">
                        <div class="name">${d.name}</div>
                        <div class="item_content">
                            <div class="item_content" id="single_item_image">
                            
                                <div class="image_container">
                                    <img src="${d.image}" width="200px" height="200px" alt="Image of ${d.name}" />
                                </div>
                           </div>
                           
                        </div>
                        <div class="item_information"> Category: ${d.category}</div>
                        <div class="item_information"> Condition: ${d.condition}</div>
                         <div class="item_information"> Location: ${d.item_location}</div>
                       <div class="item_content">
                            <div class="item_information" id="price">Starting price: $ ${priceHtml}</div>
                       </div>
                          
                    </a>`;
                });
                $('.all_items').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error){
                //TODO: SHOW toastr
                console.error(error);
            }
            })
        });
});

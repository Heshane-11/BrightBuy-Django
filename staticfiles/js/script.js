// ===============================
// GLOBAL IMAGE SWITCH FUNCTION
// ===============================
function changeImage(element) {
    const mainImage = document.getElementById("mainProductImage");

    if (mainImage) {
        mainImage.src = element.src;
    }

    document.querySelectorAll(".thumb-image").forEach(img => {
        img.classList.remove("active-thumb");
    });

    element.classList.add("active-thumb");
}



// ===============================
// jQuery ready start
// ===============================
$(document).ready(function () {

    /* ///////////////////////////////////////
       BASIC UI INTERACTIONS
    /////////////////////////////////////// */


    // Prevent dropdown from closing when clicking inside
    $(document).on('click', '.dropdown-menu', function (e) {
        e.stopPropagation();
    });


    // Radio button active state
    $('.js-check :radio').change(function () {
        const name = $(this).attr('name');
        $('input[name="' + name + '"]').closest('.js-check').removeClass('active');
        $(this).closest('.js-check').addClass('active');
    });


    // Checkbox active state
    $('.js-check :checkbox').change(function () {
        $(this).closest('.js-check').toggleClass('active', this.checked);
    });


    // Bootstrap tooltip
    if ($('[data-toggle="tooltip"]').length > 0) {
        $('[data-toggle="tooltip"]').tooltip();
    }


    // ===============================
    // AUTO-SELECT FIRST THUMBNAIL
    // ===============================
    const firstThumb = document.querySelector(".thumb-image");
    if (firstThumb) {
        firstThumb.classList.add("active-thumb");
    }

});
// ===============================
// jQuery ready end
// ===============================

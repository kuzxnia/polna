(function($) {
  "use strict"; // Start of use strict

    $(document).ready(function (){
      $(document).on('click', '.modal ul li a', function (){
        if (!$(this).parent().attr('class')) {
          $('.modal ul li').removeClass("active");
          $(this).parent().addClass("active")

          let navHref = $(this).attr('href').slice(1)
          $('.modal').find(`section`).removeClass("active")
          $('.modal').find(`section[id="${navHref}"]`).addClass("active")

        }

      })
    })
})(jQuery); // End of use strict

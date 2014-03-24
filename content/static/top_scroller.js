$(document).ready(function (){
    var $small_header = $('#small_header');
    $(document).scroll(function() {
        $small_header.css({display: $(this).scrollTop() > 160? "block":"none"});
    });
});

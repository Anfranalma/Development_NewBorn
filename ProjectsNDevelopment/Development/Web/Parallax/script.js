$(document).ready(function() {
    $(window).scroll(function() {
      var scrollTop = $(this).scrollTop();
      $('.parallax-bg').css('transform', 'translate3d(0, ' + scrollTop / 3 + 'px, 0)');
    });
  });
  
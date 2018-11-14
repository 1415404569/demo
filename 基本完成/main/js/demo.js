/**
 * Particleground demo
 * @author Jonathan Nicol - @mrjnicol
 */

$(document).ready(function() {
  $('#particles').particleground({
    dotColor: '#da4260',
    lineColor: '#da4260'
  });
  $('.intro').css({
    'margin-top': -($('.intro').height() / 2)
  });
});
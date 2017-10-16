var toSubmit = [];
var timeTaken = 0;

$(document).ready(function() {
	$(".hours-alert").hide();

	$(".todo-item").click(function() {
		// console.log($(this).attr("data-time"))
		timeTaken += parseInt($(this).attr("data-time"));
		console.log("todo item clicked")
		var newItem = $(this).clone();
		newItem.appendTo("#today-container");
		newItem.removeClass("todo-item");
		newItem.addClass("today-item");
		$(this).hide();
		toSubmit.push(this.id);
		console.log(timeTaken);
	});

	$(document).on("click", ".today-item", function() {
		console.log("today item clicked");
		console.log(this.id);
		oldId = this.id;
		timeTaken -= parseInt($(this).attr("data-time"));
		$(this).remove();
		console.log(oldId)
		$("#" + oldId.trim() + " ").show();
		$("#" + oldId.trim()).show();
		toSubmit.splice(toSubmit.indexOf(oldId), 1);
	});

	$("#task-submit").click(function() {
		console.log("submit button pushed");

		if (timeTaken != 8)
		{
			if (timeTaken > 8) 
				var msg = "Too many hours!";
			else
				var msg = "Not enough hours!";
			$(".hours-alert").html(msg)
			$(".hours-alert").show()
		}
		else
		{
			$.ajax({
				type: 'POST',
				url: '',
				data: {'toSubmit[]' : toSubmit}
			});
			location.reload()
		}
	});
});




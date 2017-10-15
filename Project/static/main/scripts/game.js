var toSubmit = [];
var timeTaken = 0;

$(document).ready(function() {
	$(".todo-item").click(function() {
		// console.log($(this).attr("data-time"))
		timeTaken += parseInt($(this).attr("data-time"));
		console.log("todo item clicked")
		var newItem = $(this).clone();
		newItem.appendTo("#today-container");
		newItem.removeClass("todo-item");
		newItem.addClass("today-item");
		$(this).toggle();
		toSubmit.push(this.id);
		console.log(timeTaken);
	});

	$(document).on("click", ".today-item", function() {
		console.log("today item clicked");
		console.log(this.id);
		oldId = this.id;
		timeTaken -= parseInt($(this).attr("data-time"));
		$(this).remove();
		$("#" + oldId).toggle();
		toSubmit.splice(toSubmit.indexOf(oldId), 1);
		console.log(timeTaken);
	});

	$("#task-submit").click(function() {
		console.log("submit button pushed");

		if (timeTaken != 8)
			alert("You have to spend 8 hours working.");
		else
			$.ajax({
				type: 'POST',
				url: '',
				data: {'toSubmit[]' : toSubmit}
			});

	});
});




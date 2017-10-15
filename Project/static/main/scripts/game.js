$(document).ready(function() {
	$(".todo-item").click(function() {
		console.log("todo item clicked")
		var newItem = $(this).clone();
		newItem.appendTo("#today-container");
		newItem.removeClass("todo-item");
		newItem.addClass("today-item");
		$(this).toggle();
	});

	$(document).on("click", ".today-item", function() {
		console.log("today item clicked");
		console.log(this.id);
		oldId = this.id;
		$(this).remove();
		$("#" + oldId).toggle();
	});
});




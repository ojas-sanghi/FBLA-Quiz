extends Node

var data := []

func _ready() -> void:
	make_quiz()

func make_quiz():
	var f = File.new()
	f.open("res://questions.json", f.READ)
	var data_text = f.get_as_text()
	f.close()

	data = parse_json(data_text)

	print(data)
	print(data.size())

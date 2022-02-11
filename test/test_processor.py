import pick_intersection as pig

def test_loading(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "a.dat"
    p.write_text("hogehoge")
    files = []
    dataset = pig.load_files(files)
    data = dataset.get_sets()
    assert len(data) == 1
    
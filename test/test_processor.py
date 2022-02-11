import pinter as pig


def test_loading(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p_a = d / "a.dat"
    p_a.write_text("[00001_FMN]\n00103_GLY  00062_THR  00046_PHE")
    p_b = d / "b.dat"
    p_b.write_text("[00002_FMN]\n00201_ILE  00197_VAL  00145_ASP")

    files = [p_a, p_b]
    dataset = pig.load_files(files)
    data = dataset.get_sets()
    assert 2 == len(data)


def test_read(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "a.dat"
    p.write_text("[00001_FMN]\n00103_GLY  00062_THR  00046_PHE")
    pairs = pig.dataset.read_pairfile(p)
    assert [
        ("00001_FMN", "00103_GLY"),
        ("00001_FMN", "00062_THR"),
        ("00001_FMN", "00046_PHE"),
    ] == pairs


def test_get_intersection(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p_a = d / "a.dat"
    p_a.write_text("[00001_FMN]\n00103_GLY  00062_THR  00046_PHE")
    p_b = d / "b.dat"
    p_b.write_text("[00001_FMN]\n00103_GLY  00046_PHE")

    files = [p_a, p_b]
    dataset = pig.load_files(files)
    dataset.create_intersection()
    intersection = dataset.intersection
    assert set([("00001_FMN", "00103_GLY"), ("00001_FMN", "00046_PHE")]) == intersection


def test_write_dat(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p_single = d / "a.dat"
    p_double = d / "b.dat"

    dataset = pig.dataset.Dataset([])
    dataset.intersection = set([("00001_FMN", "00103_GLY"), ("00001_FMN", "00046_PHE")])
    dataset.to_dat(p_single)
    assert "[00001_FMN]\n00046_PHE 00103_GLY\n" == p_single.read_text()

    dataset = pig.dataset.Dataset([])
    dataset.intersection = set(
        [
            ("00001_FMN", "00103_GLY"),
            ("00001_FMN", "00046_PHE"),
            ("00002_FMN", "00046_PHE"),
        ]
    )
    dataset.to_dat(p_double)
    assert (
        "[00001_FMN]\n00046_PHE 00103_GLY\n[00002_FMN]\n00046_PHE\n"
        == p_double.read_text()
    )

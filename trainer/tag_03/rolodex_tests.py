import rolodex

fname = "/home/coder/python_fortgeschritten/materialien/adressen.csv"

def test_rolo_is_generated():
    r = rolodex.RoloDex(fname)

    assert r.fname == fname
    assert len(r.rolo) == 3

def test_rolo_search_of_existing():
    r = rolodex.RoloDex(fname)
    search_term = "Willi"
    
    result = r.search(search_term)
    assert result["name"] == search_term

def test_rolo_result_keys():    
    r = rolodex.RoloDex(fname)
    search_term = "Willi"
    keys = ["name", "plz", "ort", "strasse"]
    result = list(r.search(search_term).keys())

    sorted(result)
    sorted(keys)

    assert result == keys 

def test_rolo_search_of_non_existing():
    r = rolodex.RoloDex(fname)

    result = r.search("Daddel")
    assert result == None

def test_add_new_address():
    r = rolodex.RoloDex(fname)

    r.new_adr({ "name": "Ulrich"})
    result = r.search("Ulrich")

    assert result["name"] == "Ulrich"
from main import TiendaOnline

def test_inventario_no_compartido():
    t1 = TiendaOnline()
    t2 = TiendaOnline()
    t1.agregar_producto("P01", "Teclado", 100, 1)
    assert len(t2.inventario) == 0
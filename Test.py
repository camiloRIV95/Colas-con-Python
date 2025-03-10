from MyQueue import MyQueue

cola = MyQueue()

cola.push(1)
cola.push(2)
cola.push(3)
cola.push(4)
cola.push(5)
cola.push(6)
cola.push(7)

print("Contenido de la cola: ", cola.showContent())
print("Elemento eliminado: ", cola.poll())
print("Contenido de la cola después del poll: ", cola.showContent())
print("Siguiente elemento a eliminar (peek):", cola.peek())

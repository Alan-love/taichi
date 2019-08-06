import taichi_lang as ti
import taichi as tc

# tc.set_gdb_trigger(True)

x, y = ti.var(ti.f32), ti.var(ti.f32)
z, w = ti.var(ti.f32), ti.var(ti.f32)
val = ti.var(ti.f32)

ti.cfg.use_llvm = True
ti.cfg.print_ir = True
# ti.runtime.print_preprocessed = True

@ti.layout
def xy():
  fork = ti.root.dense(ti.k, 128)
  fork.dense(ti.ij, 16).place(x, y)
  fork.dense(ti.ijk, 4).dense(ti.i, 8).place(z, w)
  ti.root.dense(ti.i, 128).place(val)

val[0] = 123456
print('val', val[0])

@ti.kernel
def test():
  a = 0
  for i in range(10):
    val[i] = i
    if i % 2 == 0:
      a += i
    ti.print(a)

test()


$$Z_n$$ is the positive integers from 1 to n

$$Z_n^* $$ is the positive integers from 1 to n that are coprime with n

Each element $$a \in Z_n^* $$ can produce a cyclic subgroup of $$Z_n^* $$ by doing $$a^k \pmod n$$ for incremental k from 1 until $$a^k = 1 \pmod n$$

This program draws all such cyclic subgroups out (except when $$a = 1$$, trivial) on separate canvases at a specified n.

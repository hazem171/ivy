# local
import ivy

# global
import math


def cat(tensors, dim=0, *, out=None):
    return ivy.concat(tensors, axis=dim, out=out)


def chunk(input, chunks, dim=0):
    shape = ivy.shape(input)[dim]
    if chunks > shape:
        split_size = shape
    else:
        split_size = math.ceil(shape / chunks) if shape % chunks != 0 else chunks
    return ivy.split(
        input, num_or_size_splits=split_size, axis=dim, with_remainder=True
    )


def concat(tensors, dim=0, *, out=None):
    return ivy.concat(tensors, axis=dim, out=out)


def nonzero(input, *, out=None, as_tuple=False):
    ret = ivy.nonzero(input)
    if as_tuple is False:
        ret = ivy.matrix_transpose(ivy.stack(ret))

    if ivy.exists(out):
        return ivy.inplace_update(out, ret)
    return ret


def permute(input, dims):
    return ivy.permute_dims(input, axes=dims)


def reshape(input, shape):
    return ivy.reshape(input, shape)


def squeeze(input, dim):
    if isinstance(dim, int):
        if input.shape[dim] > 1:
            return input if ivy.is_ivy_array(input) else ivy.array(input)
    return ivy.squeeze(input, dim)


def stack(tensors, dim=0, *, out=None):
    return ivy.stack(tensors, axis=dim, out=out)


def swapaxes(input, axis0, axis1):
    return ivy.swapaxes(input, axis0, axis1)


def swapdims(input, dim0, dim1):
    return ivy.swapaxes(input, dim0, dim1)


def transpose(input, dim0, dim1):
    return ivy.swapaxes(input, dim0, dim1)


def tile(input, dims):
    try:
        tup = tuple(dims)
    except TypeError:
        tup = (dims,)
    d = len(tup)
    res = 0
    if len(input.shape) > len([dims]) - 1:
        res = input
    if d < input.ndim:
        tup = (1,) * (input.ndim - d) + tup
        res = ivy.tile(input, tup)

    else:
        res = ivy.tile(input, reps=dims, out=None)
    return res

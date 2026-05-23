---
id: "class:deepxube.domains.cube3.Quaternion"
kind: "class"
name: "Quaternion"
qualified_name: "deepxube.domains.cube3.Quaternion"
module: "deepxube.domains.cube3"
file: "deepxube/domains/cube3.py"
line_start: 70
line_end: 181
is_abstract: false
is_dataclass: false
decorators: []
generic_parameters: []
bases: []
methods:
  - "func:deepxube.domains.cube3.Quaternion.from_v_theta"
  - "func:deepxube.domains.cube3.Quaternion.__init__"
  - "func:deepxube.domains.cube3.Quaternion.__repr__"
  - "func:deepxube.domains.cube3.Quaternion.__mul__"
  - "func:deepxube.domains.cube3.Quaternion.as_v_theta"
  - "func:deepxube.domains.cube3.Quaternion.as_rotation_matrix"
  - "func:deepxube.domains.cube3.Quaternion.rotate"
attributes:
  - name: "self.x"
    annotation: null
    default: null
    from: "__init__"
factory_registrations: []
docstring_source: "present"
---

# `deepxube.domains.cube3.Quaternion`

**File:** [deepxube/domains/cube3.py:70](../../../deepxube/domains/cube3.py#L70)
**Abstract:** no

## Docstring

Quaternion Rotation:

Class to aid in representing 3D rotations via quaternions.

## Inheritance

**Direct bases:**

**Subclasses:** *(populated by graph post-pass — see `graph.json`.)*

## Methods

- `from_v_theta`
- `__init__`
- `__repr__` *(trivial, skipped)* — *(no docstring)*
- `__mul__`
- `as_v_theta`
- `as_rotation_matrix`
- `rotate`

## Attributes

| Name | Type | Source |
|------|------|--------|
| `self.x` | — | __init__ |

## Source

```python
class Quaternion:
    """Quaternion Rotation:

    Class to aid in representing 3D rotations via quaternions.
    """

    @classmethod
    def from_v_theta(cls, v, theta) -> 'Quaternion':  # type: ignore
        """
        Construct quaternions from unit vectors v and rotation angles theta

        Parameters
        ----------
        v : array_like
            array of vectors, last dimension 3. Vectors will be normalized.
        theta : array_like
            array of rotation angles in radians, shape = v.shape[:-1].

        Returns
        -------
        q : quaternion object
            quaternion representing the rotations
        """
        theta = np.asarray(theta)
        v = np.asarray(v)
        s = np.sin(0.5 * theta)
        c = np.cos(0.5 * theta)

        v = v * s / np.sqrt(np.sum(v * v, -1))
        x_shape = v.shape[:-1] + (4,)

        x: NDArray = np.ones(x_shape).reshape(-1, 4)
        x[:, 0] = c.ravel()
        x[:, 1:] = v.reshape(-1, 3)
        x = x.reshape(x_shape)

        return cls(x)

    def __init__(self, x: NDArray):
        """ Store quaternion coefficients ``(w, xi, yj, zk)`` as a numpy array. """
        self.x = np.asarray(x, dtype=float)

    def __repr__(self) -> str:
        return "Quaternion:\n" + self.x.__repr__()

    def __mul__(self, other: 'Quaternion') -> 'Quaternion':
        """ :return: Hamilton product of two quaternions. """
        # multiplication of two quaternions.
        # we don't implement multiplication by a scalar
        sxr = self.x.reshape(self.x.shape[:-1] + (4, 1))
        oxr = other.x.reshape(other.x.shape[:-1] + (1, 4))

        prod = sxr * oxr
        return_shape = prod.shape[:-1]
        prod = prod.reshape((-1, 4, 4)).transpose((1, 2, 0))

        ret = np.array([(prod[0, 0] - prod[1, 1]
                         - prod[2, 2] - prod[3, 3]),
                        (prod[0, 1] + prod[1, 0]
                         + prod[2, 3] - prod[3, 2]),
                        (prod[0, 2] - prod[1, 3]
                         + prod[2, 0] + prod[3, 1]),
                        (prod[0, 3] + prod[1, 2]
                         - prod[2, 1] + prod[3, 0])],
                       dtype=float,
                       order='F').T
        return self.__class__(ret.reshape(return_shape))

    def as_v_theta(self) -> Tuple[NDArray, NDArray]:
        """Return the v, theta equivalent of the (normalized) quaternion"""
        x = self.x.reshape((-1, 4)).T

        # compute theta
        norm = np.sqrt((x ** 2).sum(0))
        theta = 2 * np.arccos(x[0] / norm)

        # compute the unit vector
        v = np.array(x[1:], order='F', copy=True)
        v /= np.sqrt(np.sum(v ** 2, 0))

        # reshape the results
        v = v.T.reshape(self.x.shape[:-1] + (3,))
        theta = theta.reshape(self.x.shape[:-1])

        return v, theta

    def as_rotation_matrix(self) -> NDArray:
        """Return the rotation matrix of the (normalized) quaternion"""
        v, theta = self.as_v_theta()

        shape = theta.shape
        theta = theta.reshape(-1)
        v = v.reshape(-1, 3).T
        c = np.cos(theta)
        s = np.sin(theta)

        mat = np.array([[v[0] * v[0] * (1. - c) + c,
                         v[0] * v[1] * (1. - c) - v[2] * s,
                         v[0] * v[2] * (1. - c) + v[1] * s],
                        [v[1] * v[0] * (1. - c) + v[2] * s,
                         v[1] * v[1] * (1. - c) + c,
                         v[1] * v[2] * (1. - c) - v[0] * s],
                        [v[2] * v[0] * (1. - c) - v[1] * s,
                         v[2] * v[1] * (1. - c) + v[0] * s,
                         v[2] * v[2] * (1. - c) + c]],
                       order='F').T
        return mat.reshape(shape + (3, 3))

    def rotate(self, points):  # type: ignore
        """ :return: ``points`` rotated by this quaternion's rotation matrix. """
        rot_mat = self.as_rotation_matrix()
        return np.dot(points, rot_mat.T)
```

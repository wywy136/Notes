# Go Basics

## Basis

### Running

File `go.mod` should be the first file for every Go project.

```go
go mod init <proj_name>
```

A dir in project is a package.

In a go file, the package name should be identical to the par dir name.

For an command line base application file, the entry file name should be `main.go` package name should be `main`, with a func named `main`

To run a go applicatoin library

```
go run <package_name>
```

### Encapsulation

By captalizing the first letter of the struct name, field name and func name, they are accessible for every file that are importing them.

### Function

Always return a pointer.

#### Multiple return values

```go
func vals() (int, int) {
    return 3, 7
}
```

#### Variadic func

```go
func sum(nums ...int) {}
```

#### Closures

```go
package main

import "fmt"

func intSeq() func() int {
    i := 0
    return func() int {
        i++
        return i
    }
}

func main() {

    nextInt := intSeq()

    fmt.Println(nextInt())
    fmt.Println(nextInt())
    fmt.Println(nextInt())

    newInts := intSeq()
    fmt.Println(newInts())
}
// 1
// 2
// 3
// 1
```

#### Interfaces

Named collections of method signatures.

We say that something *satisfies this interface* (or *implements this interface*) if it has a method with the exact signature defined in the interface.

*Wherever you see declaration in Go (such as a variable, function parameter or struct field) which has an interface type, you can use an object of any type **so long as it satisfies the interface***.

```go
package main

import (
    "fmt"
    "strconv"
    "log"
)

// Declare a Book type which satisfies the fmt.Stringer interface.
type Book struct {
    Title  string
    Author string
}

func (b Book) String() string {
    return fmt.Sprintf("Book: %s - %s", b.Title, b.Author)
}

// Declare a Count type which satisfies the fmt.Stringer interface.
type Count int

func (c Count) String() string {
    return strconv.Itoa(int(c))
}

// Declare a WriteLog() function which takes any object that satisfies
// the fmt.Stringer interface as a parameter.
func WriteLog(s fmt.Stringer) {
    log.Print(s.String())
}

func main() {
    // Initialize a Count object and pass it to WriteLog().
    book := Book{"Alice in Wonderland", "Lewis Carrol"}
    WriteLog(book)

    // Initialize a Count object and pass it to WriteLog().
    count := Count(3)
    WriteLog(count)
}
```

```go
package main

import (
    "fmt"
    "math"
)

type geometry interface {
    area() float64
    perim() float64
}

type rect struct {
    width, height float64
}
type circle struct {
    radius float64
}

func (r rect) area() float64 {
    return r.width * r.height
}
func (r rect) perim() float64 {
    return 2*r.width + 2*r.height
}

func (c circle) area() float64 {
    return math.Pi * c.radius * c.radius
}
func (c circle) perim() float64 {
    return 2 * math.Pi * c.radius
}

func measure(g geometry) {
    fmt.Println(g)
    fmt.Println(g.area())
    fmt.Println(g.perim())
}

func main() {
    r := rect{width: 3, height: 4}
    c := circle{radius: 5}

    measure(r)
    measure(c)
}
```

### Loop

#### For loop

```go
for j := 7; j <= 9; j++ {
    fmt.Println(j)
}
```

### Data Structures

#### Slices

```go
s := make([]string, 3)
s[0] = "a"
s[1] = "b"
s[2] = "c
s = append(s, "d")
c := make([]string, len(s))
copy(c, s)
l := s[2:5]
t := []string{"g", "h", "i"}
```

#### Maps

```go
m := make(map[string]int)
m["k1"] = 7
m["k2"] = 13
delete(m, "k2")
n := map[string]int{"foo": 1, "bar": 2}
```

#### Struct

Struct can have methods associated with it.

```go
type Vec2 struct {
	X int
	Y int
}

func (self *Vec2) Negate() {
	self.X = -self.X
	self.Y = -self.Y
}
```

### Range

```go
nums := []int{2, 3, 4}
for i, num := range nums {
    if num == 3 {
        fmt.Println("index:", i)
    }
}
kvs := map[string]string{"a": "apple", "b": "banana"}
for k, v := range kvs {
    fmt.Printf("%s -> %s\n", k, v)
}
for k := range kvs {
    fmt.Println("key:", k)
}
for i, c := range "go" {
    fmt.Println(i, c)
}
// 0 103
// 1 111
```


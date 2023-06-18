# Go

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

### Command-line Arguments

Starting from `os.Args[1]`.

Get input from Stdin

```go
import (
    "bufio"
    "os"
)
counts := make(map[string]int)
input := bufio.NewScanner(os.Stdin)
for input.Scan() {
    counts[input.Text()]++
}
```

Get input from files

```go
f, err := os.Open(arg)
if err != nil {
    ...
}
input := bufio.NewScanner(f)
f.Close()
```

Read from files directly

```go
import (
	"io/ioutil"
    "strings"
)
data, err := ioutil.ReadFile(filename)
for _, line := range strings.Split(string(data), "\n") {
    ...
}
```



### Encapsulation

By captalizing the first letter of the struct name, field name and func name, they are accessible for every file that are importing them.

## Function

### Function Values

A function value may be called like any other function:

```go
func square(n int) int     { return n * n }
f := square
```

### Multiple return values

```go
func vals() (int, int) {
    return 3, 7
}
```

### Variadic func

```go
func sum(nums ...int) {}
```

### Closures

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

## Data Structures

### Arrays

```go
var a[3]int  // Default with 0
q := [...]int{1, 2, 3}  // Array literal
```

### Slices

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
months := [...]string{1: "January", /* ... */, 12: "December"}
```

#### Exchange two values

```go
s[i], s[j] = s[j], s[i]
```

### Maps

```go
m := make(map[string]int)
m["k1"] = 7
m["k2"] = 13
delete(m, "k2")
n := map[string]int{"foo": 1, "bar": 2}
for key, value in range n {
    fmt.Printf("%s\t%d\n", key, value)
}

```

### Struct

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

### JSON

Converting a Go data structures to JSON is called *marshaling*, done by `json.Marshal`:

```go
import "encoding/json"
type Movie struct {
    Title  string
    Year   int  `json:"released"`
    Color  bool `json:"color,omitempty"`
    Actors []string
}
var movies = []Movie{
    {Title: "Casablanca", Year: 1942, Color: false, Actors: []string{"Humphrey Bogart", "Ingrid Bergman"}},
    {Title: "Cool Hand Luke", Year: 1967, Color: true, Actors: []string{"Paul Newman"}},
    {Title: "Bullitt", Year: 1968, Color: true, Actors: []string{"Steve McQueen", "Jacqueline Bisset"}},
}
data, err := json.Marshal(movies)
```

This produces a byte slice containing a very long string with no white space.

Can use `json.MarshalIndent` to produce neatly indented output for human readable output. Two additional arguments define a prefix for each line of output and a string for each level of indentation:

```go
data, err := json.MarshalIndent(movies, "", "    ")
```

Use field tags to define the name to be shown in the output. **Only exported fields are marshaled, which is why we chose capitalized names for all the Go field names.**

The *unmarshaling* is done by `json.Unmarshal`. 

```go
var titles []struct{ Title string }
err := json.Unmarshal(data, &titles)
```

The names of all the struct fields must be capit alized even if their JSON names are not. However, **the matching pro cess that associates JSON names with Go struct names during unmarshaling is case-insensitive, so it’s only necessary to use a field tag when there’s an underscore in the JSON name but not in the Go name.**

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

## OOD - Method

### Declarations

```go
type Point struct {X, Y float64}
func (p *Point) Distance(q *Point) float64 {
    ...
}
```

Because calling a function makes a copy of each argument value, if a function needs to update a variable, or if an argument is so large that we wish to avoid copy ing it, we must pass the address of the variable using a pointer.

**Declare all the methods with pointer-type arguments.**

### Composing Types by Struct Embedding

```go
import "image/color"
type Point struct{ X, Y float64 }
type ColoredPoint struct {
    Point
    Color color.RGBA
}
```

We can call methods of the embedded `Point` field using a receiver of type ColoredPoint, even though `ColoredPoint` has no declared methods. 

### Encapsulation

A variable or method of an object is said to be *encapsulated* if it is inaccessible to clients of the object.

In Go, capitalized identifiers are exported from the package where they are defined. 

The same mechanism that limits access to members of a package also limits access to the fields of a struct or the methods of a type. As a consequence, to encapsulate an object, we must make it a struct.

The unit of encapsulation is the package, not the type as in many other languages. The fields of a struct type are visible to all code within the same package. 

Better to unexport fields and have getters and setters defined.

## OOD - Interfaces

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

// Declare a WriteLog() function which takes any object that satisfies the fmt.Stringer interface as a parameter.
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

### Type Assertions

Applied to an interface value. 

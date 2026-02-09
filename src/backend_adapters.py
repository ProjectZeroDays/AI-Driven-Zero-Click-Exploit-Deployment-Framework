[
    { "extension": "mjs", "name": "Node Module", "command": "node '$uri'" },
    {
        "extension": "vb",
        "name": "Visual Basic",
        "command": "vbc /nologo '$name' && '$dir$nameNoExt'"
    },
    {
        "extension": "vbs",
        "name": "Visual Basics",
        "command": "cscript '$uri'"
    },
    { "extension": "scala", "name": "Scala", "command": "scala '$uri'" },
    { "extension": "jl", "name": "Julia", "command": "julia '$uri'" },
    { "extension": "cr", "name": "Crystal", "command": "crystal '$uri'" },
    { "extension": "ml", "command": "ocaml '$uri'" },
    { "extension": "exs", "name": "Elixir", "command": "elixir '$uri'" },
    {
        "extension": "hx",
        "command": "haxe --cwd '$dirNoSlash' --run '$nameNoExt'"
    },
    { "extension": "rkt", "command": "racket '$uri'" },
    { "extension": "scm", "command": "csi -script '$uri'" },
    { "extension": "ahk", "command": "autohotkey '$uri'" },
    { "extension": "au3", "command": "autoit3 '$uri'" },
    { "extension": "ipy", "name": "Ipython", "command": "ipython '$uri'" },
    {
        "extension": "kts",
        "name": "Kotlin",
        "command": "kotlinc -script '$uri'"
    },
    { "extension": "dart", "name": "Dart", "command": "dart '$uri'" },
    {
        "extension": "pas",
        "command": "fpc '$name' && '$dir$nameNoExt'"
    },
    {
        "extension": "pp",
        "command": "fpc '$name' && '$dir$nameNoExt'"
    },
    { "extension": "d", "command": "dmd '$name' && '$dir$nameNoExt'" },
    { "extension": "hs", "name": "Haskell", "command": "runhaskell '$uri'" },
    {
        "extension": "nim",
        "name": "Nim",
        "command": "nim compile --verbosity:0 --hints:off --run"
    },
    {
        "extension": "csproj",
        "name": "C-Sharp Project",
        "command": "dotnet run --project"
    },
    {
        "extension": "fsproj",
        "name": "F-Sharp Project",
        "command": "dotnet run --project"
    },
    { "extension": "kit", "command": "kitc --run" },
    { "extension": "v", "command": "v run '$uri'" },
    { "extension": "vsh", "command": "v run '$uri'" },
    {
        "extension": "sass",
        "name": "Sass",
        "command": "sass --style expanded '$uri'"
    },
    {
        "extension": "cu",
        "command": "nvcc '$name' -o '$nameNoExt' && '$dir$nameNoExt'"
    },
    { "extension": "ring", "command": "ring '$uri'" },
    { "extension": "sml", "command": "sml '$uri'" },
    {
        "extension": "js",
        "name": "Javascipt",
        "command": "node '$name'",
        "icon": "file file_type_javascript"
    },
    {
        "extension": "py",
        "name": "Python",
        "command": "python '$name'"
    },
    {
        "extension": "cpp",
        "name": "C++",
        "command": "g++ '$uri' -o '$nameNoExt' && ./'$nameNoExt'"
    },
    {
        "extension": "java",
        "name": "Java",
        "command": "javac '$uri' && java '$nameNoExt'"
    },
    { "extension": "sh", "name": "Bash", "command": "bash '$uri'" },
    {
        "extension": "c",
        "name": "C",
        "command": "gcc '$uri' -o '$nameNoExt' && ./'$nameNoExt'"
    },
    {
        "extension": "cs",
        "name": "C-Sharp",
        "command": "csc '$uri' && '$nameNoExt'"
    },
    { "extension": "php", "name": "PHP", "command": "php '$uri'" },
    { "extension": "rb", "name": "Ruby", "command": "ruby '$uri'" },
    { "extension": "swift", "name": "Swift", "command": "swift '$uri'" },
    { "extension": "go", "name": "Go Lang", "command": "go run '$uri'" },
    { "extension": "pl", "name": "Perl", "command": "perl '$uri'" },
    { "extension": "r", "name": "R Script", "command": "Rscript '$uri'" },
    { "extension": "lua", "name": "Lua", "command": "lua '$uri'" },
    { "extension": "scala", "name": "Scala", "command": "scala '$uri'" },
    {
        "extension": "kt",
        "name": "Kotlin",
        "command": "kotlinc '$uri' -include-runtime -d '$nameNoExt'.jar && java -jar '$nameNoExt'.jar"
    },
    {
        "extension": "vb",
        "name": "Visual Basics (EXE)",
        "command": "vbnc '$uri' && mono '$nameNoExt.exe'"
    },
    {
        "extension": "hs",
        "command": "ghc '$uri' -o '$nameNoExt' && ./'$nameNoExt'"
    },
    {
        "extension": "rs",
        "name": "Rust",
        "command": "rustc '$uri' && ./'$nameNoExt'"
    },
    { "extension": "ex", "name": "Elixir", "command": "elixirc '$uri'" },
    { "extension": "erl", "name": "E Script", "command": "escript '$uri'" },
    { "extension": "clj", "name": "Clojure", "command": "clojure '$uri'" },
    { "extension": "lisp", "name": "Lisp", "command": "sbcl --script '$uri'" },
    {
        "extension": "m",
        "name": "Gcc",
        "command": "gcc -framework Foundation '$uri' -o '$nameNoExt' && ./'$nameNoExt'"
    },
    { "extension": "d", "command": "dmd '$uri' && ./'$nameNoExt'" },
    { "extension": "groovy", "name": "Groovy", "command": "groovy '$uri'" },
    { "extension": "kts", "name": "K Script", "command": "kscript '$uri'" },
    {
        "extension": "sql",
        "name": "SQL (MySql)",
        "command": "mysql -u username -p < '$uri'"
    },
    { "extension": "swift", "name": "Swift", "command": "swift '$uri'" },
    {
        "extension": "matlab",
        "name": "Matlab",
        "command": "matlab -nodisplay -nosplash -r 'run('$uri');exit;'"
    },
    {
        "extension": "hs",
        "command": "ghc '$uri' -o '$nameNoExt' && ./'$nameNoExt'"
    },
    {
      
    }
]

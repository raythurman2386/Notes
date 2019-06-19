# Key organizational concepts
  `Programs`
  `namespaces`
  `types`
  `members`
  `assemblies`

  C# programs consist of one or more source files

  Programs declare types, which contain members and can be organized into namespaces.

  Clases and interfaces are examples of types.

  Fields, methods, properties, and events are examples of members.

  C# programs are compiled into assemblies
  `.exe` = applications, `.dll` = libraries

    using System;
    namespace Acme.Collections
    {
      public class Stack
      {
        Entry top;
        public void Push(object data)
        {
          top = new Entry(top, data);
        }

        public object Pop()
        {
          if(top == null)
          {
            throw new InvalidOperationException();
          }
          object result = top.data;
          top = top.next;
          return result;
        }

        class Entry
        {
          public Entry next;
          public object data;
          public Entry(Entry next, object data)
          {
            this.next = next;
            this.data = data;
          }
        }
      }
    }

  An assembly is a self-describing unit of functionality containing both code and metadata, there is no need for `#include` directives and header files in C#.
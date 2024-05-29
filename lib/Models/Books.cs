using Microsoft.AspNetCore.Mvc;

namespace WebApplicationMVC.Models
{
    [BindProperties]
    public class Book
    {
        public int id { get; set; }
        public string Title { get; set; }
        public string Author { get; set; }
        public int Edition { get; set; }
    }
}
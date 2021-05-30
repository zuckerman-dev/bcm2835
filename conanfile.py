from conans import ConanFile, CMake, tools

class bcm2835Conan(ConanFile):
   name = "bcm2835"
   version = "1.68"
   settings = "os", "compiler", "build_type", "arch"
   generators = "cmake"
   default_options = {}

   scm = {
      "type" : "git",
      "subfolder" : ".",
      "url" : "https://github.com/zuckerman-dev/bcm2835.git",
      "revision" : "auto", 
      "submodule" : "recursive"
   }
   no_copy_source = True
   keep_imports = True
      
   def build(self):
      cmake = CMake(self)
      cmake.configure()
      cmake.build()
      cmake.install()

   def package_info(self):
      self.cpp_info.includedirs = [f'include/{self.name}/{self.version}/']  # Ordered list of include paths
      self.cpp_info.libs = tools.collect_libs(self)
      
   def imports(self):
      self.copy("*.dll", dst="bin", src="bin") # From bin to bin
      self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin
      
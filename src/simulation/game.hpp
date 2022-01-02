#if !defined(KANACHAN_SIMULATION_GAME_HPP_INCLUDE_GUARD)
#define KANACHAN_SIMULATION_GAME_HPP_INCLUDE_GUARD

#include "simulation/paishan.hpp"
#include <boost/python/dict.hpp>
#include <boost/python/object.hpp>
#include <random>
#include <vector>
#include <array>
#include <utility>
#include <cstdint>


namespace Kanachan{

void simulateGame(
  std::mt19937 &urng, std::uint_fast8_t room, bool dong_feng_zhan,
  std::array<std::pair<std::uint_fast8_t, boost::python::object>, 4u> const &seats,
  boost::python::object external_tool,
  std::vector<Kanachan::Paishan> const &test_paishan_list,
  boost::python::dict result);

} // namespace Kanachan

#endif // !defined(KANACHAN_SIMULATION_GAME_HPP_INCLUDE_GUARD)
